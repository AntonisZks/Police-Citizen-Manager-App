; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Police Citizen Manager"
#define MyAppVersion "1.0"
#define MyAppPublisher "Zks Industries"
#define MyAppURL "https://www.zks_code.gr"
#define MyAppExeName "PoliceCitizenManager.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{1198DB1C-24FF-4AAA-A1E7-9139B8D91333}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=C:\Users\Antonis\Desktop\Citizens\dist\License\license.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\Antonis\Desktop\Citizens
OutputBaseFilename=PoliceCitizenManager_WINDOWS_1.0_setup
SetupIconFile=C:\Users\Antonis\Desktop\windows-installer-icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Antonis\Desktop\Citizens\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Antonis\Desktop\Citizens\Files\*"; DestDir: "{app}/Files"; Flags: ignoreversion recursesubdirs createallsubdirs; Permissions: everyone-full
Source: "C:\Users\Antonis\Desktop\Citizens\Imgs\*"; DestDir: "{app}/Imgs"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Antonis\Desktop\Citizens\Info_about_app\*"; DestDir: "{app}/Info_about_app"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Antonis\Desktop\Citizens\License\*"; DestDir: "{app}/License"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Antonis\Desktop\Citizens\Password\*"; DestDir: "{app}/Password"; Flags: ignoreversion recursesubdirs createallsubdirs ; Permissions: everyone-full
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

