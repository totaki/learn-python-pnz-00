import React, { useRef, useState } from "react";


const send = ({ current }, callback) => {
  const getValue = name => {
    return current.elements.namedItem(name).value;
  };

  const sendEvent = ({url}) => {
    alert(url);
    let event = {
      "title": getValue("title"),
      "body": getValue("body"),
      "event_time": getValue("event_time"),
      "place": url
    };

    fetch('http://127.0.0.1:8000/api/v1/events/', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json; charset=utf-8'
      },
      body: JSON.stringify(event)
    })
      .then(response => response.json())
      .then(json => callback(json.args))


  };

  let place = {
      "place_name": getValue("place_name"),
      "city": getValue("city"),
      "street": getValue("street"),
      "house_number": getValue("house_number"),
      "office_number": getValue("office_number"),
    };

  fetch('http://127.0.0.1:8000/api/v1/places/', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json; charset=utf-8'
      },
      body: JSON.stringify(place)
    })
      .then(response => response.json())
      .then(json => sendEvent(json));

  };

export default function SendForm() {
  const [result, setResult] = useState({});
  const formRef = useRef(null);

  return (
    <form className="App" ref={formRef} id="_sone">
      <input type="text" name="place_name" placeholder="place_name" />
      <input type="text" name="city" placeholder="city" />
      <input type="text" name="street" placeholder="street" />
      <input type="text" name="house_number" placeholder="house_number" />
      <input type="text" name="office_number" placeholder="office_number" />
      <input type="text" name="title" placeholder="title" />
      <input type="text" name="body" placeholder="body" />
      <input type="text" name="event_time" placeholder="2019-12-12T19:00:00Z" />
      <button onClick={() => send(formRef, setResult)}>Send</button>
    </form>
  );
}