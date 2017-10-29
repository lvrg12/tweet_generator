//connection.js
var prompt = require('prompt');
prompt.start();

prompt.get(['username'], function (err, result)
{
    if (result.username != null)
    {
        var spawn = require('child_process').spawn,
        py    = spawn('python', ['tweet_generator.py']),
        data = result.username,
        dataString = '';
        
        py.stdout.on('data', function(data)
        {
            dataString += data.toString();
        });
        py.stdout.on('end', function()
        {
            console.log('\nThis are the generated tweets:\n')
            console.log(dataString);
        });
        py.stdin.write(JSON.stringify(data));
        py.stdin.end();
    }
  });