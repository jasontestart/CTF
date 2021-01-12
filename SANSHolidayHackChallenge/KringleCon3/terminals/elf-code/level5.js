elf.moveTo(lollipop[1]);
elf.moveTo(lollipop[0]);
var data = elf.ask_munch(0);
var answer = data.filter(elem => typeof elem === 'number');
elf.tell_munch(answer);
elf.moveUp(2);
