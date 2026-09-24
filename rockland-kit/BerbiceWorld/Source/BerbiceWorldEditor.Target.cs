using UnrealBuildTool;
using System.Collections.Generic;

public class BerbiceWorldEditorTarget : TargetRules
{
	public BerbiceWorldEditorTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		DefaultBuildSettings = BuildSettingsVersion.Latest;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		ExtraModuleNames.Add("BerbiceWorld");
	}
}
