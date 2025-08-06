6/27/25 - v1
made the thing

7/2/25 - v1.1
added 16 character limit warnings for both batch version and single version
plus readme

7/7/25 - v1.2
its supposed to be 15 >:(

8/6/25 - v1.3
made 15-char checks into functions, to allow them to loop back if needed.

----------------------------------------------
this script was written by Brandon Jadue, partially derived from
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-computer?view=powershell-7.5

hello. please note prior to using this script that if the target is in an Azure AD domain setting, then it must be already registered to the domain.

also, be aware that some programs and services limit the computer name to 16 characters.
if the new name is above 16 characters, there are warnings. theyre obnoxious. they should be.
ignore at your own risk.

