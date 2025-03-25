import './App.css'
import { Layout } from './layout/layout'
import fundo from './assets/fundo.png'

function App() {
  return (
    <>
      <Layout />
      <div className='position-relative'>
        <div className='bg-black bg-opacity-50'>
          <div id="carouselExampleControls" className="carousel slide" data-bs-ride="carousel">
            <div className="carousel-inner">
              <div className="carousel-item active">
                <img className='w-100 opacity-50' height={800} src={fundo} alt="" />
                <div className='position-absolute top-0 start-0 text-white'>
                  <h1 className='mx-5 mt-5'>Bem-vindo(a) à FarmeWork</h1>
                  <h2 className='mx-5'>Aqui você encontra serviços e produtos personalizados para seu problema</h2>
                </div>
              </div>
              <div className="carousel-item">
                <img className='w-100 opacity-50' height={800} src={fundo} alt="" />
                <div className='position-absolute top-0 start-0 text-white'>
                  <h1 className='mx-5 mt-5'>2</h1>
                  <h2 className='mx-5'>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius architecto, modi incidunt sapiente repudiandae saepe vero ipsa iusto voluptatibus aut quisquam tempora quibusdam illo eos et, dolorum magnam consequuntur quod?</h2>
                </div>
              </div>
              <div className="carousel-item">
                <img className='w-100 opacity-50' height={800} src={fundo} alt="" />
              </div>
              <div className="carousel-item">
                <img className='w-100 opacity-50' height={800} src={fundo} alt="" />
              </div>
              <div className="carousel-item">
                <img className='w-100 opacity-50' height={800} src={fundo} alt="" />
              </div>
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
    </>
  )
}

export default App
