#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "CantaCheckpoint.generated.h"

class UBoxComponent;

/**
 * One gate on the CANTA KART seawall road.
 * Index 0 is the start/finish line. Higher indices are passed in order.
 */
UCLASS()
class BERBICEWORLD_API ACantaCheckpoint : public AActor
{
	GENERATED_BODY()

public:
	ACantaCheckpoint();

	/** 0 = start/finish. Place gates so indices increase along the lap. */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Canta Kart")
	int32 CheckpointIndex = 0;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Canta Kart")
	TObjectPtr<UBoxComponent> Trigger;

protected:
	virtual void BeginPlay() override;

	UFUNCTION()
	void OnTriggerBeginOverlap(UPrimitiveComponent* OverlappedComp, AActor* OtherActor,
		UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep,
		const FHitResult& SweepResult);
};
