#!/usr/bin/node
function myArgument(){
    const numArgument = arguments.length;
    if (numArgument == 0){
        console.log('No argument')
    }
    else if (numArgument == 1){
        console.log('Argument found')
    }
    else{
        console.log('Arguments found')
    }
}
