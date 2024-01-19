let scene, renderer, camera
let cube


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
}
function add_cube(){
    const geometry = new THREE.BoxGeometry(10, 1, 10) // 幾何體
    const material = new THREE.MeshPhongMaterial({
        color: 0x0000ff
    }) // 材質
    cube = new THREE.Mesh(geometry, material) // 建立網格物件
    cube.position.set(0, 0, 0)
    scene.add(cube)
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
        this.bodyGeo = new THREE.BoxGeometry(1,1,1)
        this.bodyMat = new THREE.MeshPhongMaterial({
            color:0x00ff00
        })
        this.car_body = new THREE.Mesh(this.bodyGeo, this.bodyMat)
        this.car_body.position.set(pos.x, pos.y, pos.z)
        scene.add(this.car_body)
        return this.car_body
    }
}

function animate(){
    //cube.rotation.x += 0.01
    //cube.rotation.y += 0.01
}

function render() {
    animate()
    requestAnimationFrame(render)
    renderer.render(scene, camera)
}

window.addEventListener("resize", function(){
    camera.aspect = window.innerWidth/window.innerHeight
    camera.updateProjectionMatrix()
    renderer.setSize(window.innerWidth, window.innerHeight)
})



init_env()
add_cube()
const car = new Car(new pos(0,1,0))


render()
