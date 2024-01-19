import * as THREE from "three"
import  {OrbitControls} from "three/examples/jsm/controls/OrbitControls";

class Car{
    constructor(x,y,z) {
        this.Geo = new THREE.BoxGeometry(1,1,1)
        this.Mat = new THREE.MeshBasicMaterial({
            color:0xff0000
        })
        this.body = new THREE.Mesh(this.Geo, this.Mat)
        this.body.position.set(x,y,z)
        scene.add(this.body)
    }
    moveX(x){
        this.body.position.x = x
    }
    moveY(x){
        this.body.position.y = x
    }
}

const renderer = new THREE.WebGLRenderer()
renderer.setClearColor(0xeeeeee, 1.0)
renderer.setSize(window.innerWidth, window.innerWidth)
document.body.appendChild(renderer.domElement)

const scene = new THREE.Scene()

const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
)
camera.position.set(0,10,10)
const orbit = new OrbitControls(camera, renderer.domElement)
orbit.update()

const grid = new THREE.GridHelper(50,50)
scene.add(grid)

const car = new Car(0,0.5,0)

function animate(){
    window.addEventListener("keydown",function (e){
        switch (e.key){

        }
    })
    renderer.render(scene, camera)
}

renderer.setAnimationLoop(animate)
