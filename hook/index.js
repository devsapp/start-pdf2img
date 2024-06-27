async function preInit(inputObj) {
    console.log(`
        ____  ____  _________   ______  _________
       / __ \\/ __ \\/ ____/__ \\ /  _/  |/  / ____/
      / /_/ / / / / /_   __/ / / // /|_/ / / __  
     / ____/ /_/ / __/  / __/_/ // /  / / /_/ /  
    /_/   /_____/_/    /____/___/_/  /_/\\____/   
                                             
`)
}

async function postInit(inputObj) {
    console.log(`\n    Welcome to the start-bottle application
     This application requires to open these services: 
         FC : https://fc.console.aliyun.com/
     
     Tips：
         - FC3 Component: https://docs.serverless-devs.com/user-guide/aliyun/#fc3
         
     * 额外说明：
     * 进行项目之后，可使用 s deploy 进行项目部署
     * 可以通过invoke命令进行相关的触发：s invoke\n`)
}

module.exports = {
    postInit,
    preInit
}