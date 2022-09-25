import React from 'react'
import Box from '@material-ui/core/Box';
import './App.css';





export const Header = (props) => {

  return (
    <header id='header'>
      <div className='intro'>
        <div className='overlay'>
          <div className='container'>
            <div className='row'>
              <div className='col-md-8 col-md-offset-2 intro-text'>
                <svg height="200" width="200">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
  Sorry, your browser does not support inline SVG.  
                </svg>
                
                {/*First Moduled Tabloid*/}
                
                <div className='Test'>
                  <a
                    href='#features'
                    className='btn btn-custom btn-lg page-scroll'
                    onClick={console.log('I was clicked!')}>
                    <div className='tabloid-box'>
                      <div className='top-row'>
                        <p id='caseName'>{props.data ? props.data.case_title : 'Loading'}</p>
                        <p id='caseDate'>{props.data ? props.data.date : 'Loading'}</p>
                        <p id='caseDocket'>{props.data ? props.data.docket : 'Loading'}</p>
              
                      </div>

                      <div className='summary'> 
                        <p id='caseSummary'>{props.data ? props.data.summary : 'Loading'}</p>
                      </div>
                        
                     
                      <div>{props.data.justices.map((justices) => {
                    
                        return (
                          <div className='justicesName'>
                            <div className='name'><p>{justices.name}</p></div>   
                            <div className='justices'><span>{justices.opinion}</span></div>
                          </div>
                        )
                      })}
                      </div>
                          {/* <p>{props.data ? props.data.justices[0].name : 'Loading'}</p>
                    <p>{props.data ? props.data.justices[0].opinion : 'Loading'}</p>
                    {/*mapper(props.data.justices)*/} 
                      
                    </div>
  
                  </a>{' '}
                </div>
                
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    
  )

}

