document.addEventListener("DOMContentLoaded", function(event) {
    
    var items = document.getElementsByClassName("item-container")
    var view = document.getElementsByClassName("items-view")
//    console.log(items)
    
    var cnt = 0
    
    for (i=0;i<items.length;i++){
        // Gather data from item
        var thisChild = items[i].children[0].children[0]
        // console.log(thisChild)
        
        // Assign data to new node
        var thisItem = document.createElement("div")
            thisItem.classList = "prod-container col-sm-6 col-md-4 col-lg-4"
            thisItem.style.height = "40em"
        var thisPic = document.createElement("img")
            thisPic.src = thisChild.src
            thisPic.title = thisChild.title
            thisPic.alt = thisChild.alt
        thisItem.appendChild(thisPic)
        var thisDesc = document.createElement("H2")
            thisDesc.innerHTML = thisChild.title
        thisItem.appendChild(thisDesc)
        
        // var thisChild = item.children[1].children[2]
        var thisPrice = items[i].getElementsByClassName("price-current")[0].innerHTML
        
        thisPrice = thisPrice.replace(/\D/g,'');
        thisPrice = (Number(thisPrice)+15000)/100
        
        var thisPrise = document.createElement("H2")
            thisPrise.innerHTML = "$"+thisPrice

//        console.log(thisPrice.innerHTML.substring(loc,end))
        
        thisItem.appendChild(thisPrise)
        
        
        
        view[0].replaceChild(thisItem,items[i])
//        console.log(items[i])
                
    }
    
    var items = document.getElementsByClassName("item-container")
    for (j=0;j<5;j++){
        for (i=0;i<items.length;i++){
            view[0].removeChild(items[i])
        }
    }
    
  });