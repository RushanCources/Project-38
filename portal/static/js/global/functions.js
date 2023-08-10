function genDiv(num, parent, cname, parentName=null, child=null, childName=null) {
    // let cont = document.createElement("div");
    // cont.id = cname;
    // document.body.appendChild(cont);
    let bget = document.getElementById(cname);
    let cget;
    console.log('first let')
    for (let i = 0; i < num; i++) {
        console.log(`${i} let in cicle`)
        let block = document.createElement(parent);
        if(parentName==null){
            block.classList.add(`parentName`);
            block.id = `parentName${i}`;
        }else{
            block.classList.add(parentName);
            block.id = `${parentName}${i}`;
        }
        bget.appendChild(block);
        if (parentName == null) {
            cget = document.getElementById(`parentName${i}`);
        } else {
            cget = document.getElementById(`${parentName}${i}`);
        }
        if(child!=null){
            let bchild = document.createElement(child);
            if(childName==null){
                bchild.id = `childName${i}`;
                bchild.classList.add(`childName`);
            }else{
                bchild.id = `${childName}${i}`;
                bchild.classList.add(childName);
            }
            cget.appendChild(bchild);
        }
    }
}


export {genDiv};