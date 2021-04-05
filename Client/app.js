
function get_bath()
{
    bath = document.getElementsByName("bath")
    for(i in bath){
     if(bath[i].checked)
     {
         return bath[i]+1
     }
    }
 return -1
}

function get_bhk()
{
    bhk = document.getElementsByName("bhk")
    for(i in bhk){
     if(bhk[i].checked)
     {
         return bhk[i]+1
     }
    }
 return -1
}


function onClickedEstimatePrice(){
    var sqft =  document.getElementById("uiSqft");
    var bhk=get_bhk();
    var bath=get_bath();
    var locations=document.getElementById("uiLocations");

    url="/api/predict_home_price"
    $.post(url,{
        total_sqft:parseFloat(sqft.value),
        bhk:"2",
        bath:"2",
        location:locations.value}
        ,function(data,status)
       {
         if(data)
         {
            document.getElementById("uiEstimatedPrice").innerHTML = "<h2>"+data.estimated_price.toString()+" Lakhs </h2>";
            console.log(status);
         }
       });

}

function onPageLoad(){
   var url = "/api/get_location"
   $.get(url,function(data,status)
   {
    if(data){
        locations = data.locations
        for(i in locations){
           opt = new Option(locations[i]);
           $("#uiLocations").append(opt);
        }
    }
   });
}


window.onload = onPageLoad