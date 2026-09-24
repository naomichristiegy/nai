#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "TimeTrialGameMode.generated.h"

class ACantaCheckpoint;

DECLARE_DYNAMIC_MULTICAST_DELEGATE_TwoParams(FOnLapCompleted, int32, LapNumber, float, LapTime);
DECLARE_DYNAMIC_MULTICAST_DELEGATE_OneParam(FOnTrialFinished, float, TotalTime);
DECLARE_DYNAMIC_MULTICAST_DELEGATE(FOnTrialStarted);

/**
 * CANTA KART 3-lap time trial on the New Amsterdam seawall road.
 * Checkpoints register themselves; the pink lap timer widget binds to the events below.
 */
UCLASS()
class BERBICEWORLD_API ATimeTrialGameMode : public AGameModeBase
{
	GENERATED_BODY()

public:
	ATimeTrialGameMode();

	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Time Trial")
	int32 TotalLaps = 3;

	UPROPERTY(BlueprintReadOnly, Category = "Time Trial")
	int32 CurrentLap = 0;

	UPROPERTY(BlueprintReadOnly, Category = "Time Trial")
	int32 NextCheckpointIndex = 0;

	UPROPERTY(BlueprintReadOnly, Category = "Time Trial")
	TArray<float> LapTimes;

	UPROPERTY(BlueprintReadOnly, Category = "Time Trial")
	float BestLapTime = 0.f;

	UPROPERTY(BlueprintReadOnly, Category = "Time Trial")
	bool bTrialRunning = false;

	UPROPERTY(BlueprintReadOnly, Category = "Time Trial")
	bool bTrialFinished = false;

	UPROPERTY(BlueprintAssignable, Category = "Time Trial")
	FOnTrialStarted OnTrialStarted;

	UPROPERTY(BlueprintAssignable, Category = "Time Trial")
	FOnLapCompleted OnLapCompleted;

	UPROPERTY(BlueprintAssignable, Category = "Time Trial")
	FOnTrialFinished OnTrialFinished;

	void RegisterCheckpoint(ACantaCheckpoint* Checkpoint);
	void CheckpointPassed(ACantaCheckpoint* Checkpoint, APawn* Pawn);

	/** Seconds elapsed in the lap in progress. 0 before the first crossing of the start line. */
	UFUNCTION(BlueprintPure, Category = "Time Trial")
	float GetCurrentLapTime() const;

	/** Sum of finished laps plus the lap in progress. */
	UFUNCTION(BlueprintPure, Category = "Time Trial")
	float GetTotalTime() const;

	UFUNCTION(BlueprintPure, Category = "Time Trial")
	int32 GetCheckpointCount() const { return Checkpoints.Num(); }

	/** "1:23.456" formatting for the pink lap timer. */
	UFUNCTION(BlueprintPure, Category = "Time Trial")
	static FString FormatLapTime(float Seconds);

	UFUNCTION(BlueprintCallable, Category = "Time Trial")
	void ResetTrial();

private:
	UPROPERTY()
	TArray<TObjectPtr<ACantaCheckpoint>> Checkpoints;

	float LapStartTime = 0.f;
	float TrialStartTime = 0.f;
};
