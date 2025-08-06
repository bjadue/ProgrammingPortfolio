#written by Brandon Jadue, in part from
#https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-computer?view=powershell-7.5

$lessThan15 = $true
$15response = "y"
#default variables regarding the target name being above 15 characters
function Get-Length {
	if ($nombre.length -gt 15){
		$lessThan15 = $false
		Write-Host "`nWARNING: `nNew host name of target PC is longer than 15 characters. This can cause issues with Azure AD, SQL, etc.." -ForegroundColor red -BackgroundColor black
		$15response = Read-Host "Type [n] to cancel this process and correct the name, otherwise press enter" 
	}
	if ($nombre.length -lt 15) {
		$lessThan15 = $true
		Write-Host "`nNew name is good. Continuing..." -ForegroundColor Green 
		return 
	}
	if ($15response -eq "n"){
		Redo-Length
	}else{
		Write-Host "`nUser opted to continue." -ForegroundColor Yellow 
		return 
	}
}
function Redo-Length {
	$nombre = Read-Host "Please enter new host name of target PC [15>= characters]"
	Write-Host "`nVerifying..." -ForegroundColor Magenta
	Get-Length
}

write-output "Please note that target PC must already be added to the domain.`n"
$target = Read-Host "Please enter host name of target PC"
$nombre = Read-Host "Please enter new host name of target PC"
Get-Length
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
rename-computer @renameParams
