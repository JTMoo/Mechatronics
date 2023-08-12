fetch("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Filadelfia?unitGroup=metric&key=YOUR_API_KEY&contentType=json", {
  "method": "GET",
  "headers": {
  }
  })
.then(response => {
  console.log(response);
})
.catch(err => {
  console.error(err);
});
