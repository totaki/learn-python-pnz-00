import React, {useEffect, useState} from 'react';
import {getItems} from "./api";

const PLACES_ROUTE = 'places';

function Place({ place_name, city, street, house_number }) {
  return (
    <div className="col-md-4">
          <div className="card mb-4 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">{place_name}</h5>
              <p className="card-text">{city}, {street}, {house_number}</p>
            </div>
          </div>
        </div>

  )
}

function Places() {
   const [places, setPlaces] = useState([]);
   const [path, _] = useState('/places/');

   useEffect(() => {
     getItems({ path }, (j) => setPlaces(j.results))
   }, [path]);

   return (
    <>
      <div className="container">
        <div className="my-h1"><h2 style={{textAlign: "center"}}>Список заведений</h2></div>
          <div className="container">
            <div className="row">
              {places.map((e, i) => <Place {...e}/>)}
            </div>
          </div>
      </div>
    </>
  )
}

export default Places
export {
  PLACES_ROUTE
}
