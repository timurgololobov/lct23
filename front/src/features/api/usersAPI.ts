import { UserApplyType } from "../../types/UserApplyType";
import { UserType } from "../../types/types";
import { api } from "./api";

export const usersApi = api.injectEndpoints({
  endpoints: (builder) => ({
    getAllUsers: builder.query<UserType[], void>({
      query: () => ({
        url: "api/users",
        method: "GET",
      }),
    }),
    getUser: builder.query<UserType, string>({
      query: (id) => ({
        url: `api/users/${id}`,
        method: "GET",
      }),
    }),
    editUser: builder.mutation<string, UserType>({
      query: (user) => ({
        url: `api/users/edit/${user.id}`,
        method: "PUT",
        body: user,
      }),
    }),
    removeUser: builder.mutation<string, string>({
      query: (id) => ({
        url: `api/users/remove/${id}`,
        method: "POST",
        body: { id },
      }),
    }),
    addUser: builder.mutation<UserType, UserType>({
      query: (user) => ({
        url: "api/users/add",
        method: "POST",
        body: user,
      }),
    }),
    getUserApply: builder.query<UserApplyType, string>({
      query: (id) => ({
        url: `api/users/apply/${id}`,
        method: "GET",
      }),
    }),
    confirmUserApply: builder.mutation<UserApplyType[], React.Key[]>({
      query: (userIds) => ({
        url: `api/users/apply/confirm`,
        method: "POST",
        body: { userIds },
      }),
    }),
    getAllUsersApply: builder.query<UserApplyType[], any>({
      query: () => ({
        url: `api/users-all/apply/`,
        method: "GET",
      }),
    }),
    addUserApply: builder.mutation<UserApplyType, UserApplyType>({
      query: (apply) => ({
        url: "api/users/apply/add",
        method: "POST",
        body: apply,
      }),
    }),
    getApplyForUserFromHR: builder.query<UserApplyType, string>({
      query: (id) => ({
        url: `api/users-from-hr/apply/${id}`,
        method: "GET",
      }),
    }),
  }),
});

export const {
  useAddUserMutation,
  useGetAllUsersQuery,
  useGetUserQuery,
  useEditUserMutation,
  useRemoveUserMutation,
  useGetUserApplyQuery,
  useAddUserApplyMutation,
  useGetAllUsersApplyQuery,
  useGetApplyForUserFromHRQuery,
  useConfirmUserApplyMutation,
} = usersApi;

export const {
  endpoints: {
    getAllUsers,
    getUser,
    editUser,
    removeUser,
    addUser,
    getUserApply,
    addUserApply,
    getAllUsersApply,
    getApplyForUserFromHR,
    confirmUserApply,
  },
} = usersApi;
