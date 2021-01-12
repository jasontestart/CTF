for (var i = 0; i < 4; i++) {
  elf.moveTo(lollipop[i]);
}
elf.moveTo(lever[0]);
var data = elf.get_lever(0);
var first = ["munchkins rule"];
var answer = first.concat(data);
elf.pull_lever(answer);
elf.moveDown(3);
elf.moveLeft(6);
elf.moveUp(3);
