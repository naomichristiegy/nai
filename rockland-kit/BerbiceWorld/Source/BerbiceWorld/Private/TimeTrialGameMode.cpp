#include "TimeTrialGameMode.h"
#include "CantaCheckpoint.h"
#include "Engine/World.h"

ATimeTrialGameMode::ATimeTrialGameMode()
{
	PrimaryActorTick.bCanEverTick = false;
}

void ATimeTrialGameMode::RegisterCheckpoint(ACantaCheckpoint* Checkpoint)
{
	if (!Checkpoint || Checkpoints.Contains(Checkpoint))
	{
		return;
	}
	Checkpoints.Add(Checkpoint);
	Checkpoints.Sort([](const ACantaCheckpoint& A, const ACantaCheckpoint& B)
	{
		return A.CheckpointIndex < B.CheckpointIndex;
	});
}

void ATimeTrialGameMode::CheckpointPassed(ACantaCheckpoint* Checkpoint, APawn* Pawn)
{
	if (!Checkpoint || !Pawn || bTrialFinished || Checkpoints.Num() == 0)
	{
		return;
	}

	// Gates must be taken in order. Anything else is ignored (wrong way, cutting the seawall).
	if (Checkpoint->CheckpointIndex != NextCheckpointIndex)
	{
		return;
	}

	const float Now = GetWorld()->GetTimeSeconds();

	if (Checkpoint->CheckpointIndex == 0)
	{
		if (!bTrialRunning)
		{
			bTrialRunning = true;
			CurrentLap = 1;
			TrialStartTime = Now;
			LapStartTime = Now;
			LapTimes.Reset();
			OnTrialStarted.Broadcast();
		}
		else
		{
			const float LapTime = Now - LapStartTime;
			LapTimes.Add(LapTime);
			if (BestLapTime <= 0.f || LapTime < BestLapTime)
			{
				BestLapTime = LapTime;
			}
			OnLapCompleted.Broadcast(CurrentLap, LapTime);

			if (CurrentLap >= TotalLaps)
			{
				bTrialRunning = false;
				bTrialFinished = true;
				OnTrialFinished.Broadcast(Now - TrialStartTime);
				return;
			}
			CurrentLap++;
			LapStartTime = Now;
		}
	}

	NextCheckpointIndex = (NextCheckpointIndex + 1) % Checkpoints.Num();
}

float ATimeTrialGameMode::GetCurrentLapTime() const
{
	if (!bTrialRunning)
	{
		return 0.f;
	}
	return GetWorld()->GetTimeSeconds() - LapStartTime;
}

float ATimeTrialGameMode::GetTotalTime() const
{
	if (!bTrialRunning && !bTrialFinished)
	{
		return 0.f;
	}
	float Total = 0.f;
	for (float T : LapTimes)
	{
		Total += T;
	}
	return Total + GetCurrentLapTime();
}

FString ATimeTrialGameMode::FormatLapTime(float Seconds)
{
	Seconds = FMath::Max(0.f, Seconds);
	const int32 Minutes = FMath::FloorToInt(Seconds / 60.f);
	const float Rem = Seconds - Minutes * 60.f;
	return FString::Printf(TEXT("%d:%06.3f"), Minutes, Rem);
}

void ATimeTrialGameMode::ResetTrial()
{
	bTrialRunning = false;
	bTrialFinished = false;
	CurrentLap = 0;
	NextCheckpointIndex = 0;
	LapTimes.Reset();
	LapStartTime = 0.f;
	TrialStartTime = 0.f;
}
