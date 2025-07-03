#THIS VERSION IS FOR DEMONSTRATION PURPOSES ONLY!
#written by Brandon Jadue, in part from
#https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-computer?view=powershell-7.5
	
write-output "Please note that target PC must already be added to the domain.`n"
$target = Read-Host "Please enter host name of target PC"
$nombre = Read-Host "Please enter new host name of target PC"
$creds = get-credential

$renameParams = @{
    ComputerName = "$target"
    NewName = "$nombre"
    DomainCredential = $creds
    Force = $true
    PassThru = $true
    Restart = $true
}
#run cmdlet with the pre-defined parameters
write-output "Process will not actually execute. DEMO ONLY`n"
rename-computer @renameParams -WhatIf
exit 0