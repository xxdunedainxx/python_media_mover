# Helper Script to get drive space #
param(
	[string]$drive=""
)
write-host (Get-PSDrive $drive | Select-Object Used,Free).Free