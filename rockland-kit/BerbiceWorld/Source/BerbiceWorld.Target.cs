using UnrealBuildTool;
using System.Collections.Generic;

public class BerbiceWorldTarget : TargetRules
{
	public BerbiceWorldTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		DefaultBuildSettings = BuildSettingsVersion.Latest;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		ExtraModuleNames.Add("BerbiceWorld");
	}
}
