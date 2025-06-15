const loginQuery = `
  SELECT * FROM public.users WHERE username = $1
`;
const registerQuery = `
  INSERT INTO public.users (username, created_at, email, password) VALUES ($1, $2, $3, $4) RETURNING *
`;

const userFoundQuery = `
  SELECT * FROM public.users WHERE email = $1
`;
module.exports = {
  loginQuery,
  registerQuery,
  userFoundQuery
};