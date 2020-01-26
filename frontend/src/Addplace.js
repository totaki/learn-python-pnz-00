import React, { useRef} from "react";
import { useHistory } from "react-router-dom";

const send = ({current}, callback) => {
  const getValue = name => {
    return current.elements.namedItem(name).value;
  };

  let place = {
    "place_name": getValue("place_name"),
    "city": getValue("city"),
    "street": getValue("street"),
    "house_number": getValue("house_number"),
    "office_number": getValue("office_number"),
  };
  const token = window.localStorage.getItem('token');

  fetch('http://127.0.0.1:8000/api/v1/private/places', {
    method: 'POST',
    headers: {
      'Content-type': 'application/json; charset=utf-8',
      'Authorization': `Token ${token}`
    },
    body: JSON.stringify(place)
  })
    .then(response => response.json())
    .then(json => callback(json));

};

function PlaceForm() {
  const formRef = useRef(null);
  const history = useHistory()

  return (
    <>
    <form className="App" ref={formRef} id="placeForm">
      <div className="form-row">
        <div className="form-group col-md-4">
          <label htmlFor="inputAddress">Место проведения</label>
          <input type="text" className="form-control" name="place_name" placeholder="Название" value="Test place"/>
        </div>
      </div>
      <div className="form-row">
        <div className="form-group col-md-4">
          <label htmlFor="inputCity">Город</label>
          <input type="text" className="form-control" name="city" value="Penza"/>
        </div>
        <div className="form-group col-md-4">
          <label htmlFor="inputStreet">Улица</label>
          <input type="text" className="form-control" name="street" value="Moskovskiy"/>
        </div>
        <div className="form-group col-md-2">
          <label htmlFor="inputHouse">Дом</label>
          <input type="text" className="form-control" name="house_number" value="10"/>
        </div>
        <div className="form-group col-md-2">
          <label htmlFor="inputOffice">Офис</label>
          <input type="text" className="form-control" name="office_number" value="10"/>
        </div>
      </div>
    </form>
    <button className="btn btn-primary" onClick={() => send(formRef, () => history.push('/places'))}>Send</button>
    </>
  );
}

export default function AddPlace() {
  return (
      <>
        <div className="container">
          <div className="my-h1">
            <h3 style={{textAlign: "center", marginBottom: 30, marginTop: 20}}>
              Форма для добавления Событий
            </h3>
          </div>
            <PlaceForm />
        </div>
      </>
    )
}


