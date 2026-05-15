# Make API request with image file
$imagePath = "C:\Senior Research Project 2025-2026\test_road_image.jpg"

# Use Invoke-WebRequest to POST the image to the analyze endpoint
$form = @{
    image = Get-Item -Path $imagePath
}

try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/analyze" `
        -Method POST `
        -Form $form `
        -UseBasicParsing
    
    # Parse and display the response
    Write-Host "API Response Status: $($response.StatusCode)"
    Write-Host "Response Content:`n"
    
    $jsonResponse = $response.Content | ConvertFrom-Json
    $jsonResponse | ConvertTo-Json -Depth 10
}
catch {
    Write-Host "Error: $($_.Exception.Message)"
}
