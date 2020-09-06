
# $jobt=New-JobTrigger -Daily -At(Get-Date).AddMinutes(1) -RepetitionInterval '00:01:00' -RepetitionDuration ([TimeSpan]::MaxValue)
$jobt=New-JobTrigger -Once -At(Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Day 1) -RepetitionDuration ([TimeSpan]::MaxValue)
Register-ScheduledJob -Name testsender4 -ScriptBlock {python D:\GitReposity\Python001-class01\week10\2CleanData\cleandata.py} -Trigger $jobt

# Unregister-ScheduledJob testsender4