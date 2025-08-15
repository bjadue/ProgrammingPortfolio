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
$target = Read-Host "Please enter current host name of target PC"
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
# SIG # Begin signature block
# MIIFhgYJKoZIhvcNAQcCoIIFdzCCBXMCAQExCzAJBgUrDgMCGgUAMGkGCisGAQQB
# gjcCAQSgWzBZMDQGCisGAQQBgjcCAR4wJgIDAQAABBAfzDtgWUsITrck0sYpfvNR
# AgEAAgEAAgEAAgEAAgEAMCEwCQYFKw4DAhoFAAQU6UTXcDBG1PGRdH07VxWmiGt+
# j1egggMjMIIDHzCCAgegAwIBAgIQSvSpUlboCYNOQ8FtH5hKxTANBgkqhkiG9w0B
# AQsFADAYMRYwFAYDVQQDDA1CcmFuZG9uIEphZHVlMB4XDTI1MDgxNTE1MzMxMFoX
# DTI2MDgxNTE1NTMxMFowGDEWMBQGA1UEAwwNQnJhbmRvbiBKYWR1ZTCCASIwDQYJ
# KoZIhvcNAQEBBQADggEPADCCAQoCggEBAMNENVjUuolxQaAW3/SBE6ophDDAxrcW
# TODklkLUOroBkfwXFbRnRsfNuzeoKpvdqmRphrDwHlhbFBHZJ3gkJ3slQvNyGjLZ
# jLqFibGdpJ7flCyPnkrR/+2i7+qf9914q3Ckcwd68hpnXXt3zSK7VZUl79hf4s1m
# T7Yvz338zvE/XIDuN7wU5l52FI1nXRU6Qm92hHqDubao29CE4ggAAn9R4AEeGiGr
# Cqx3NbUvtAwX4Wr76zWKUtd+JSP+oYGx1oubMOVRz/PQwola3eoS9YLNefjQnsC9
# bIjOi7VnIazsTOkeApN0pB2Qou4Nr59PC6aT2ayBdNkgqTqVQa3f5PUCAwEAAaNl
# MGMwDgYDVR0PAQH/BAQDAgeAMBMGA1UdJQQMMAoGCCsGAQUFBwMDMB0GA1UdEQQW
# MBSCEnd3dy5iamFkdWUyMTguaW5mbzAdBgNVHQ4EFgQU8BtiKMhmjyWNibwY2Ns/
# mio6yjYwDQYJKoZIhvcNAQELBQADggEBAKu5c813lI5S0Ee0oRfFVmU4JE409zDB
# gN15pZ+mcH/BMfZHF5R4Hrh4ZLjq8sAfJ6zFEbkHbA+PJlKABFeve6Diryhq/UXa
# zr5kw12qXirYjRNGAdKRi4h6rcevGhCbSapPN3GRnin0iZ6JlApfkbP9jes45IjT
# vfxzn2K2P8U9x6nQgeFWKeAhHjovS/autnaznx6ogILMsUaak46cem3/5diKNzcP
# QzUSA6nbMgYtuGA0A1sbP+yquyuIkM6/SdSri7RM4xpytns2fpcZV6O4Nk7rBz3D
# +Dg6s0i0UBHGqpo9E2UUuxsx1cLCbpv1csQf9FvgNIg2wXQQh41Kzi4xggHNMIIB
# yQIBATAsMBgxFjAUBgNVBAMMDUJyYW5kb24gSmFkdWUCEEr0qVJW6AmDTkPBbR+Y
# SsUwCQYFKw4DAhoFAKB4MBgGCisGAQQBgjcCAQwxCjAIoAKAAKECgAAwGQYJKoZI
# hvcNAQkDMQwGCisGAQQBgjcCAQQwHAYKKwYBBAGCNwIBCzEOMAwGCisGAQQBgjcC
# ARUwIwYJKoZIhvcNAQkEMRYEFH8YykDPR6aJ4prIJYRhLnL6UCHMMA0GCSqGSIb3
# DQEBAQUABIIBAGlzSFOLAcy2qTt7ma2gw1Y8wjfRucY4r+G1qk5VQUSPej+4dOer
# NgQCmiEuFCXwrFV95PE4BLB/wYH9UrEsl1udH7xmcbcrvGCXx5mML/3DREKEGDm9
# RfeMnuq9nACZBj9tZrUUWzv9xCgowWxAiOcynJmeDuAKx4BH2MKKs44zkgrDM1dJ
# Jl+xDPrdYLaxh2EMQ4Gw2tQcBhw89N8NU9elLybol5HmRrDCdsk6Kg12rKE/aDj+
# g33ru7Wuhe40wep2e0Q/ivIJUQQbMRWIN630gkU/2gzAe8Fkzl18v7DpzXEe4vNH
# kKoQJOpT/nQA7nrtTWAHhn+9ndPDUXEx+HE=
# SIG # End signature block
