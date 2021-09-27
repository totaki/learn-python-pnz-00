import React, {useEffect, useState}  from "react";


function Pagination(props){
  return (
    <>
      <div role="group" aria-label="paginationGroup">
        <button  type="button" className="btn btn-secondary pagination-previous"  onClick={
          () => props.setURL(props.previous)}>
          Previous
        </button>
        {props.next ? <button  type="button" className="btn btn-secondary pagination-next" onClick={
          () => props.setURL(props.next)} >
          Next
        </button> : null}
      </div>
    </>
  )
}

export default Pagination
