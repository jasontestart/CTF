for (var i = 0; i < 4; i++) {
  elf.moveTo(lollipop[i]);
}
elf.moveTo(munchkin[0]);
var data = elf.ask_munch(0);
for (x in data) {
  var val = data[x];
  if (val == 'lollipop') {
    elf.tell_munch(x);
  }
}
elf.moveUp(2)
