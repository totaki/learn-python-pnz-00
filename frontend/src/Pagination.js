import React, {useEffect, useState}  from "react";


function Pagination(props){

  return (
    <>
      <div className="btn-group" role="group" aria-label="paginationGroup">
        {props.p ? <button  type="button" className="btn btn-secondary" onClick={() => props.setURL(props.p)}>Previous</button> : null}
        {props.n ? <button  type="button" className="btn btn-secondary" onClick={() => props.setURL(props.n)}>Next</button> : null}
      </div>
    </>
  )
}

export default Pagination
