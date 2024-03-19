import { Link, Outlet } from "react-router-dom";

function RootLayout() {
  return (
    <>
      <Link to={"/"}>Home</Link> | <Link to={"/about"}>About</Link> |{" "}
      <Link to={"/airdrop"}>Airdrop</Link>
      <Outlet />
    </>
  );
}

export default RootLayout;
