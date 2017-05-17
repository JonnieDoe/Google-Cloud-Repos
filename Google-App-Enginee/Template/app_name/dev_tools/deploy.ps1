param(
[string]$version
)

If($version){
	Write-Host $version
	appcfg.py update --version=$version --oauth2_credential_file=.appcfg_oauth2_tokens .
} Else {
	#Write-Host 'is empty'
	appcfg.py update --oauth2_credential_file=.appcfg_oauth2_tokens .
}
# Execute npm commands
npm install
npm run start