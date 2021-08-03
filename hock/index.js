async function preInit(inputObj) { }

async function postInit(inputObj) {
  console.log(`  
        ____  ____  _________   ______  _________
       / __ \\/ __ \\/ ____/__ \\ /  _/  |/  / ____/
      / /_/ / / / / /_   __/ / / // /|_/ / / __  
     / ____/ /_/ / __/  / __/_/ // /  / / /_/ /  
    /_/   /_____/_/    /____/___/_/  /_/\\____/
`)
  console.log(`
    Welcome to the start-pdf2img application
      This application requires to open these services: 
          FC : https://fc.console.aliyun.com/
      This application can help you quickly build a function calculation project based on GhostScript and GraphicsMagick.
      It should have used a function from PDF to IMG as an example, so that you can have some understanding of custom runtime and dependent installation, and you can also develop on the basis of this application.
      This application can help you quickly deploy the Laravel project:
          Full yaml configuration: https://github.com/devsapp/laravel#%E5%AE%8C%E6%95%B4yaml
          Laravel development docs : https://learnku.com/docs/laravel/8.x
      This application homepage: https://github.com/devsapp/start-pdf2img
`)
}

module.exports = {
  postInit,
  preInit
}