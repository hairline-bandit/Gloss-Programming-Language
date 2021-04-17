param ($file)

Start-Process "python" -ArgumentList "main.py $file" -Wait -NoNewWindow
Start-Process "go" -ArgumentList "run 123123123123.go" -Wait -NoNewWindow

Remove-Item "123123123123.go"