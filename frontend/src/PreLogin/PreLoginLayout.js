import React from "react";
import NavBar from "./NavBar";
import { Outlet } from "react-router-dom";
export default function PreLoginLayout() {
  return (
    <div>
      <NavBar />
      <Outlet />
    </div>
  );
}
