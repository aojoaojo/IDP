import fundo from '../assets/fundo.png'
import HandsPlanting from '../assets/Hands Nurturing Plant.jpeg'
import FarmerInField from '../assets/Farmer Standing in Field.jpeg'
import Technician from '../assets/Technician Walking in Solar Farm at Sunset.jpeg'
import BulbInSoil from '../assets/Bulb in Soil Close-Up.jpeg'
import { CardOverCarrossel } from './cardOverCarrossel'

export function Carrossel() {
    return (
        <div className='position-relative'>
            <div>
                <div id="carouselExampleControls" className="carousel slide" data-bs-ride="carousel">
                    <div className="carousel-inner">

                        <div className="carousel-item active">
                            <img className='w-100 object-fit-cover' height={820} src={HandsPlanting} alt="" />
                            <CardOverCarrossel titulo='Bem-vindo(a) à FarmeWork' texto='Aqui você encontra serviços e produtos personalizados para seu problema' />
                        </div>

                        <div className="carousel-item">
                            <img className='w-100 object-fit-cover' height={820} src={fundo} alt="" />
                            <CardOverCarrossel titulo='Bem-vindo(a) à FarmeWork' texto='Aqui você encontra serviços e produtos personalizados para seu problema' />                        </div>

                        <div className="carousel-item">
                            <img className='w-100 object-fit-cover' height={820} src={FarmerInField} alt="" />
                            <CardOverCarrossel titulo='Bem-vindo(a) à FarmeWork' texto='Aqui você encontra serviços e produtos personalizados para seu problema' />                        </div>

                        <div className="carousel-item">
                            <img className='w-100 object-fit-cover' height={820} src={Technician} alt="" />
                            <CardOverCarrossel titulo='Bem-vindo(a) à FarmeWork' texto='Aqui você encontra serviços e produtos personalizados para seu problema' />                        </div>

                        <div className="carousel-item">
                            <img className='w-100 object-fit-cover' height={820} src={BulbInSoil} alt="" />
                            <CardOverCarrossel titulo='Bem-vindo(a) à FarmeWork' texto='Aqui você encontra serviços e produtos personalizados para seu problema' />                        </div>

                    </div>
                    <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                        <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span className="visually-hidden">Previous</span>
                    </button>
                    <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                        <span className="carousel-control-next-icon" aria-hidden="true"></span>
                        <span className="visually-hidden">Next</span>
                    </button>
                </div>
            </div>
        </div>
    )
}