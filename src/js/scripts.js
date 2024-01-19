import * as THREE from "three"


function init_env(){
    scene = new THREE.Scene()
    renderer = new THREE.WebGLRenderer()
    renderer.setSize(window.innerWidth/1.2, window.innerHeight/1.2)
    renderer.setClearColor(0xeeeeee, 1.0)
    renderer.shadowMap.enable = true

    document.body.appendChild(renderer.domElement)

    camera = new THREE.PerspectiveCamera(
        50,
        window.innerWidth/window.innerHeight,
        0.1,
        100
    )
    camera.position.set(10,10,10)
    camera.lookAt(scene.position)


    let pointLight = new THREE.PointLight(0xffffff)
    pointLight.position.set(10, 10, 10)
    scene.add(pointLight)

    window.addEventListener("resize", function(){
    camera.aspect = window.innerWidth/window.innerHeight
    camera.updateProjectionMatrix()
    renderer.setSize(window.innerWidth, window.innerHeight)
    })
}
function add_floor(){
    const geometry = new THREE.BoxGeometry(10, 1, 10) // 幾何體
    const material = new THREE.MeshPhongMaterial({
        color: 0x0000ff
    })
    let cube = new THREE.Mesh(geometry, material)
    cube.position.set(0, 0, 0)
    scene.add(cube)
    return cube
}
class pos{
    constructor(x,y,z) {
        this.x = x
        this.y = y
        this.z = z
    }
}
class Car{
    constructor(pos) {
        this.Geo = new THREE.BoxGeometry(1,1,1)
        this.Mat = new THREE.MeshPhongMaterial({
            color:0x00ff00
        })
        this.body = new THREE.Mesh(this.Geo, this.Mat)
        this.body.position.set(pos.x, pos.y, pos.z)
        scene.add(this.body)
    }
    move_x(x){
        this.body.position.x = x
        camera.position.x = this.body.position.x+10
    }
    move_z(z){
        this.body.position.z = z
        camera.position.z = this.body.position.z+10
    }
}

function render() {
    animate()
    //cameraControl.update()
    requestAnimationFrame(render)
    renderer.render(scene, camera)
}


let scene, camera, renderer
init_env()

let floor,car1
floor = add_floor()
car1 = new Car(new pos(0,1,0))



function animate(){
    window.addEventListener("keydown", function (e){
        switch (e.key){
            case "w":
                car1.move_x(car1.body.position.x+0.01)
                break;
            case "s":
                car1.move_x(car1.body.position.x-0.01)
                break
            case "a":
                car1.move_z(car1.body.position.z+0.01)
                break
            case "d":
                car1.move_z(car1.body.position.z-0.01)
                break
        }
    })
}


render()
