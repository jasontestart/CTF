Invoke-WebRequest http://127.0.0.1:1225/api/off
$correct_gases_postbody = @{O=6;H=7;He=3;N=4;Ne=22;Ar=11;Xe=10;F=20;Kr=8;Rn=9}
Invoke-WebRequest http://127.0.0.1:1225/api/refraction?val=1.867
Invoke-WebRequest http://127.0.0.1:1225/api/temperature?val=-33.5
Invoke-WebRequest http://127.0.0.1:1225/api/angle?val=65.5
Invoke-WebRequest -Method POST -Body $correct_gases_postbody  http://localhost:1225/api/gas
Invoke-WebRequest http://127.0.0.1:1225/api/on
(Invoke-WebRequest http://127.0.0.1:1225/api/output).RawContent
