# Arrays
arrays are a list from variables

look at this example:

```bash
$names = ['parsa', 'pashmak', 'jack'];

println $names; # output: ['parsa', 'pashmak', 'jack']
println $names[0]; # output: parsa
println $names[1]; # output: pashmak
println $names[2]; # output: jack
```

this is a example about array and loop:

```bash
$names = ['parsa', 'pashmak', 'jack'];

$i = 0;

loop
    println $names[$i];
    $i = $i + 1;
while $i < len($names);
```

output:

```
parsa
pashmak
jack
```

the above code prints names one by one

### arraypush
you can add new item to a array:

```bash
$myarray = ['red', 'green', 'blue'];
println $myarray; # output: ['red', 'green', 'blue']

mem 'yellow'; arraypush $myarray ^; # add mem (^) to the $myarray
println $myarray; # output: ['red', 'green', 'blue', 'yellow']
```

`arraypush` operation gets two argument: array and new item you want to add to the array

### arraypop
you can delete a item from array:

```bash
$myarray = ['red', 'green', 'blue'];
println $myarray; # output: ['red', 'green', 'blue']

mem 1; arraypop $myarray ^; # remove index mem (^) from $myarray
println $myarray; # output: ['red', 'blue']
```

`arraypop` operation gets two argument: array and index of that item you want to be remove from array
