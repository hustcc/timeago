if (!process.argv[2]){
    console.log('No file')
    return;
}
var test = require('./'+process.argv[2])
var fs = require('fs');
var dir = './tmp';

if (!fs.existsSync(dir)){
    fs.mkdirSync(dir);
}

var statements = []

for(var i = 0; i<14; i++){
    statements.push(test(null, i))
}

result  = {statements: statements};

fs.writeFileSync(dir+'/'+process.argv[2].split('/').pop().replace('.js', '')+'.json', JSON.stringify(result))
