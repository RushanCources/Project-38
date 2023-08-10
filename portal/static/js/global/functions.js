function genDiv(num, parent, parentName, child, childName, cname) {
    // let cont = document.createElement("div");
    // cont.id = cname;
    // document.body.appendChild(cont);
    let bget = document.getElementById(cname);
    console.log('first let')
    for (let i = 0; i < num; i++) {
        console.log(`${i} let in cicle`)
        let block = document.createElement(parent);
        block.classList.add(parentName);
        block.id = `bl${i}`;
        let bchild = document.createElement(child);
        bchild.classList.add(childName);
        bget.appendChild(block);
        let cget = document.getElementById(`bl${i}`);
        cget.appendChild(bchild);
    }
}


export {genDiv};