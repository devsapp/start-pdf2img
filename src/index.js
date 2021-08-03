const { fromPath } = require('pdf2pic')
const fs = require('fs')

exports.handler = (event, context, callback) => {
  if(!fs.existsSync('/tmp/images')) fs.mkdirSync('/tmp/images')

  const options = {
    saveFilename: "page",
    savePath: "/tmp/images",
    format: "jpg",
    // density: 100,
    width: 1000,
    height: 1414
  }

  const filePath = '/code/test.pdf'
  const pageNumber = 1
  const isBase64 = false

  fromPath(filePath, options).bulk(pageNumber, isBase64).then(r => {
    console.log(r)
    callback(null, 'convert success.')
  }).catch(e => {
    console.error(e)
    callback(null, 'convert fail.')
  })
}