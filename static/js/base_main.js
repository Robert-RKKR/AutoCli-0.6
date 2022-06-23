// LEFT PANEL ACTION - CLOSE / OPEN MENU WITH COOKIES:
var toggleButtons = document.getElementsByClassName("menu_collapse_link");
var cookies = document.cookie.split(";");
 
for(let i=0; i<cookies.length; i++) {
    let cookie = cookies[i].split("=");
    if(cookie[0] === "open_menu_action" || cookie[0] === " open_menu_action") {
        if(cookie[1] != "false") {
            let menu_number = parseInt(cookie[1]);
            for(let i=0; i<toggleButtons.length; i++) {
                if(i === menu_number) {
                    let toggleButton = toggleButtons[i];
                    let activeElement = toggleButtons[i].nextElementSibling;
                   
                    activeElement.classList.remove("collapse");
                }
            }
        }
    }
}
 
for(let i=0; i<toggleButtons.length; i++) {
    let toggleButton = toggleButtons[i];
    let activeElement = toggleButtons[i].nextElementSibling;
 
    toggleButton.addEventListener("click", function(event) {
       
        if(activeElement.classList.contains("collapse") === false) {
            activeElement.classList.add("collapse");
            document.cookie = "open_menu_action=false;path=/";
        } else {
            for(let i=0; i<toggleButtons.length; i++) {
                let activeElementInside = toggleButtons[i].nextElementSibling
                activeElementInside.classList.add("collapse");
            }
            activeElement.classList.remove("collapse");
            document.cookie = "open_menu_action=" + i + ";path=/";
        } 
 
    });
 
}

// LEFT PANEL ACTION - SHOW HIDE WHOLE MENU:
var mainMenu = document.getElementById("page_left");

mainMenu.addEventListener("mouseenter", function(event) {
    hideMenu();
    console.log("hideMenu")
});

mainMenu.addEventListener("mouseleave", function(event) {
    showMenu();
    console.log("showMenu")
});

function hideMenu() {
    var menuLinks = document.getElementsByClassName("menu_link");
    var menuLinkTexts = document.getElementsByClassName("menu_link_text");

    // Add class to menu link:
    for(let i=0; i<menuLinks.length; i++) {
        let menuLink = menuLinks[i]
        menuLink.classList.add("menu_link_hidden");
    }
    // Add class to menu link text:
    for(let i=0; i<menuLinkTexts.length; i++) {
        let menuLinkText = menuLinkTexts[i]
        menuLinkText.classList.add("menu_link_text_hidden");
    }

}

function showMenu() {
    var menuLinks = document.getElementsByClassName("menu_link");
    var menuLinkTexts = document.getElementsByClassName("menu_link_text");

    // Add class to menu link:
    for(let i=0; i<menuLinks.length; i++) {
        let menuLink = menuLinks[i]
        menuLink.classList.remove("menu_link_hidden");
    }
    // Add class to menu link text:
    for(let i=0; i<menuLinkTexts.length; i++) {
        let menuLinkText = menuLinkTexts[i]
        menuLinkText.classList.remove("menu_link_text_hidden");
    }

}
