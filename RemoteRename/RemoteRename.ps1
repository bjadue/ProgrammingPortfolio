#written by Brandon Jadue, in part from
#https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-computer?view=powershell-7.5
$lessThan15 = $true
$15response = "y"
#default variables regarding the target name being above 15 characters
function Get-Length {
	Write-Host "`nVerifying new name $nombre..." -ForegroundColor Magenta
	if ($nombre.length -gt 15){
		Write-Host "$nombre did not pass check." -ForegroundColor Red
		$lessThan15 = $false
		Write-Host "`nWARNING: `nNew host name of target PC is longer than 15 characters. This can cause issues with Azure AD, SQL, etc.." -ForegroundColor red -BackgroundColor black
		$15response = Read-Host "Type [n] to cancel this process and correct the name, otherwise press enter`n" 
	}else{
		$lessThan15 = $true  
	}
	if ($15response -eq "n" -and $lessThan15 -eq $false){
		Redo-Length
	}elseif($15response -ne "n" -and $lessThan15 -eq $false){
		#user force bypass
		Write-Host "User opted to continue." -ForegroundColor Yellow 
		return
	}elseif($lessThan15 -eq $true){
		Write-Host "Name is good. Continuing..." -ForegroundColor Green
		return
	}else{
 		Write-Host "`nFatal error. Aborting." -ForegroundColor red -BackgroundColor black
 		exit 1
  	}
}
function Redo-Length {
	$nombre = ""
 	#reset variable, to prevent any issues in case it does not change
	$nombre = Read-Host "Please enter new host name of target PC [15>= characters]"
	Get-Length($nombre)
}
write-output "Please note that target PC must already be added to the domain.`n"
$target = Read-Host "Please enter host name of target PC"
$nombre = Read-Host "Please enter new host name of target PC"
#entering potential loop
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
