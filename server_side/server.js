const hapi = require('@hapi/hapi')

const init = async ()=>{
    const server = hapi.server({
        host : "localhost",
        port : 5000,
        routes : {
            cors : {
                origin : ["*"]
            }
            }
    })

    await server.start()
    console.log(`server berjalan di ${server.info.uri}`)
} 

init()