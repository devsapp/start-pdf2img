async function preInit(inputObj) {

}

async function postInit(inputObj) {
    console.log(`
        ____  ____  _________   ______  _________
       / __ \\/ __ \\/ ____/__ \\ /  _/  |/  / ____/
      / /_/ / / / / /_   __/ / / // /|_/ / / __  
     / ____/ /_/ / __/  / __/_/ // /  / / /_/ /  
    /_/   /_____/_/    /____/___/_/  /_/\\____/   
                                             
`)
    console.log(`\n    Welcome to the start-pdf2img application
     This application requires to open these services: 
         FC : https://fc.console.aliyun.com/
     This application can help you quickly deploy the an application that can convert pdf into an image.
     This application has a GhostScript & GraphicsMagick environment, and you can develop it on the basis of this application.
     This application homepage: https://github.com/devsapp/start-pdf2img\n`)
}

module.exports = {
    postInit,
    preInit
}