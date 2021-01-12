function right(steps) {
	elf.moveRight(steps)
}

function left(steps) {
	elf.moveLeft(steps)

}

function pull(lever,oldsum) {
	var newsum = oldsum + elf.get_lever(lever)
	elf.pull_lever(newsum)
	elf.moveUp(2)
	return newsum
}

function get_lollipop(array) {
        function findit(key_str, obj) {
		for (key in obj) {
			key_str += (obj[key] == "lollipop") ? key : ""
		}
		return key_str
	}
        return array.reduce(findit,"")
}

var sum = 0
var sidestep = 1
for (var i = 0;  i < 5; i += 2) {
	right(sidestep)
	sum = pull(i,sum)
	sidestep += 2
	left(sidestep)
	sum = pull(i+1,sum)
	sidestep += 2
}
elf.tell_munch(get_lollipop)
right(sidestep)
