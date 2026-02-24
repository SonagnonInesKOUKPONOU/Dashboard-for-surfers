from surf_scrap import scrape_surf_report

url = "https://www.surf-report.com/meteo-surf/carcans-plage-s1013.html"
output_path = "carcans_surf_data.csv"
scrape_surf_report(url, output_path)