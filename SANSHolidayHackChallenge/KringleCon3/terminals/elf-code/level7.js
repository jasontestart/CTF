function pull(lever) { 
	elf.pull_lever(lever)
}

function up(steps) {
	elf.moveUp(steps)
}

function munch_sum(array) {
	return array.reduce((a,b) => a.concat(b),[]).filter(elem => typeof elem === 'number').reduce((c,d) => c+d,0)
}
for (var i=1; i < 7; i+=4) {
	elf.moveDown(i)
	pull(i-1)
	elf.moveLeft(i+1)
	pull(i)
	up(i+2)
	pull(i+1)
	elf.moveRight(i+3)
	pull(i+2)
}
up(2)
elf.moveLeft(4)
elf.tell_munch(munch_sum)
up(2)
