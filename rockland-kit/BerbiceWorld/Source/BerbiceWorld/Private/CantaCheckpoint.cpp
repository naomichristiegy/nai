#include "CantaCheckpoint.h"
#include "TimeTrialGameMode.h"
#include "Components/BoxComponent.h"
#include "GameFramework/Pawn.h"
#include "Kismet/GameplayStatics.h"

ACantaCheckpoint::ACantaCheckpoint()
{
	PrimaryActorTick.bCanEverTick = false;

	Trigger = CreateDefaultSubobject<UBoxComponent>(TEXT("Trigger"));
	SetRootComponent(Trigger);
	// Wide enough to span a two-lane road, tall enough that a jumping kart still counts.
	Trigger->SetBoxExtent(FVector(100.f, 800.f, 400.f));
	Trigger->SetCollisionProfileName(TEXT("OverlapAllDynamic"));
	Trigger->SetGenerateOverlapEvents(true);
}

void ACantaCheckpoint::BeginPlay()
{
	Super::BeginPlay();

	Trigger->OnComponentBeginOverlap.AddDynamic(this, &ACantaCheckpoint::OnTriggerBeginOverlap);

	if (ATimeTrialGameMode* GM = Cast<ATimeTrialGameMode>(UGameplayStatics::GetGameMode(this)))
	{
		GM->RegisterCheckpoint(this);
	}
}

void ACantaCheckpoint::OnTriggerBeginOverlap(UPrimitiveComponent*, AActor* OtherActor,
	UPrimitiveComponent*, int32, bool, const FHitResult&)
{
	APawn* Pawn = Cast<APawn>(OtherActor);
	if (!Pawn)
	{
		return;
	}

	if (ATimeTrialGameMode* GM = Cast<ATimeTrialGameMode>(UGameplayStatics::GetGameMode(this)))
	{
		GM->CheckpointPassed(this, Pawn);
	}
}
