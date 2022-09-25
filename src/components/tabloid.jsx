const createTabloid = (props) => {
    return (
        <div id='tabloid'>
            <div className='container'>
                <button>
                    <div className='row'>
                        <h5>{props.date}</h5><h5>{props.date}</h5>
                    </div>
                </button>
            </div>


        </div>
    )
    

}

export default createTabloid;